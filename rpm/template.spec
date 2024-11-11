%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-pal-gripper-controller-configuration
Version:        3.4.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS pal_gripper_controller_configuration package

License:        Apache License 2.0
URL:            https://github.com/pal-robotics/tiago_simulation
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-humble-controller-manager
Requires:       ros-humble-joint-trajectory-controller
Requires:       ros-humble-position-controllers
Requires:       ros-humble-ros-workspace
BuildRequires:  ros-humble-ament-cmake-auto
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-humble-ament-lint-auto
BuildRequires:  ros-humble-ament-lint-common
%endif

%description
The pal_gripper_controller_configuration package

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/humble" \
    -DAMENT_PREFIX_PATH="/opt/ros/humble" \
    -DCMAKE_PREFIX_PATH="/opt/ros/humble" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Mon Nov 11 2024 TIAGo support team <tiago-support@pal-robotics.com> - 3.4.0-1
- Autogenerated by Bloom

* Fri Aug 09 2024 TIAGo support team <tiago-support@pal-robotics.com> - 3.3.0-1
- Autogenerated by Bloom

* Tue Jun 25 2024 TIAGo support team <tiago-support@pal-robotics.com> - 3.2.0-1
- Autogenerated by Bloom

* Fri Jan 19 2024 TIAGo support team <tiago-support@pal-robotics.com> - 3.1.0-1
- Autogenerated by Bloom

* Mon Dec 18 2023 TIAGo support team <tiago-support@pal-robotics.com> - 3.0.7-1
- Autogenerated by Bloom

* Mon Apr 17 2023 TIAGo support team <tiago-support@pal-robotics.com> - 3.0.4-1
- Autogenerated by Bloom

* Fri Mar 17 2023 TIAGo support team <tiago-support@pal-robotics.com> - 3.0.3-1
- Autogenerated by Bloom

* Wed Feb 08 2023 TIAGo support team <tiago-support@pal-robotics.com> - 3.0.2-1
- Autogenerated by Bloom

* Thu Dec 15 2022 TIAGo support team <tiago-support@pal-robotics.com> - 3.0.1-1
- Autogenerated by Bloom

* Thu Oct 27 2022 TIAGo support team <tiago-support@pal-robotics.com> - 3.0.0-1
- Autogenerated by Bloom

